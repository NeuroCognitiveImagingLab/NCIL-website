import Foundation
import Vision
import CoreImage
import AppKit

// Emits one JSON object per input image:
//   {"file":..., "w":..., "h":..., "faces":[{"x","y","w","h","eyeX","eyeY"}]}
// All coordinates are in PIXELS with origin at the TOP-LEFT, so the consumer
// never has to think about Vision's bottom-left normalized space.

func analyze(_ path: String) -> [String: Any] {
    guard let img = NSImage(contentsOfFile: path),
          let tiff = img.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiff),
          let cg = rep.cgImage
    else { return ["file": path, "error": "unreadable"] }

    let W = Double(cg.width), H = Double(cg.height)
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    let req = VNDetectFaceLandmarksRequest()
    do { try handler.perform([req]) }
    catch { return ["file": path, "w": W, "h": H, "error": "\(error)"] }

    var faces: [[String: Any]] = []
    for obs in (req.results ?? []) {
        let b = obs.boundingBox                       // normalized, bottom-left origin
        let fx = b.minX * W
        let fw = b.width * W
        let fh = b.height * H
        let fy = (1.0 - b.maxY) * H                   // flip to top-left origin

        // Eye midpoint, if landmarks resolved; else fall back to upper third of the box.
        var eyeX = fx + fw / 2.0
        var eyeY = fy + fh * 0.42
        if let lm = obs.landmarks {
            var pts: [CGPoint] = []
            for region in [lm.leftEye, lm.rightEye] {
                if let r = region { pts.append(contentsOf: r.normalizedPoints.map { CGPoint(x: CGFloat($0.x), y: CGFloat($0.y)) }) }
            }
            if !pts.isEmpty {
                // landmark points are normalized WITHIN the face bounding box
                let mx = pts.map { Double($0.x) }.reduce(0,+) / Double(pts.count)
                let my = pts.map { Double($0.y) }.reduce(0,+) / Double(pts.count)
                eyeX = fx + mx * fw
                eyeY = fy + (1.0 - my) * fh
            }
        }
        faces.append(["x": fx, "y": fy, "w": fw, "h": fh, "eyeX": eyeX, "eyeY": eyeY])
    }
    return ["file": path, "w": W, "h": H, "faces": faces]
}

var out: [[String: Any]] = []
for path in CommandLine.arguments.dropFirst() { out.append(analyze(path)) }
let data = try! JSONSerialization.data(withJSONObject: out, options: [.prettyPrinted])
print(String(data: data, encoding: .utf8)!)
