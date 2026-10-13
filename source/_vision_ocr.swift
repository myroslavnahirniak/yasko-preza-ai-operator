import Foundation
import Vision
import AppKit

struct OCRLine: Codable { let text:String; let confidence:Float; let x:Double; let y:Double; let w:Double; let h:Double }
struct OCRResult: Codable { let path:String; let lines:[OCRLine]; let error:String? }
var results:[OCRResult]=[]
for arg in CommandLine.arguments.dropFirst() {
    do {
        let req=VNRecognizeTextRequest()
        req.recognitionLevel = .accurate
        req.usesLanguageCorrection = true
        let langs=try req.supportedRecognitionLanguages()
        req.recognitionLanguages = ["ru-RU","en-US"].filter { langs.contains($0) }
        let handler=VNImageRequestHandler(url:URL(fileURLWithPath:arg),options:[:])
        try handler.perform([req])
        let lines=(req.results ?? []).compactMap { o -> OCRLine? in
            guard let c=o.topCandidates(1).first else{return nil}
            let b=o.boundingBox
            return OCRLine(text:c.string,confidence:c.confidence,x:b.origin.x,y:b.origin.y,w:b.size.width,h:b.size.height)
        }
        results.append(OCRResult(path:arg,lines:lines,error:nil))
    } catch { results.append(OCRResult(path:arg,lines:[],error:String(describing:error))) }
}
let encoder=JSONEncoder();encoder.outputFormatting=[.prettyPrinted,.sortedKeys,.withoutEscapingSlashes]
FileHandle.standardOutput.write(try encoder.encode(results))
