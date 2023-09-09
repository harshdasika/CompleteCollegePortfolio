//
// F# image processing functions.
//
//
// Harsh Dasika, 652855943, hdasik2, 11/29/22
//

namespace ImageLibrary

module Operations =
  //
  // all functions must be indented
  //

  //
  // Grayscale:
  //
  // Converts the image into grayscale and returns the 
  // resulting image as a list of lists. Pixels in grayscale
  // have the same value for each of the Red, Green and Blue
  // values in the RGB value.  Conversion to grayscale is done
  // by using a WEIGHTED AVERAGE calculation.  A normal average
  // (adding the three values and dividing by 3) is not the best,
  // since the human eye does not perceive the brightness of 
  // red, green and blue the same.  The human eye perceives 
  // green as brighter than red and it perceived red as brighter
  // than blue.  Research has shown that the following weighted
  // values should be used when calculating grayscale.
  //  - the green value should account for 58.7% of the grayscale.
  //  - the red value should account for   29.9% of the grayscale.
  //  - the blue value should account for  11.4% of the grayscale.
  //
  // So if the RGB values were (25, 75, 250), the grayscale amount 
  // would be 80, (25 * 0.299 + 75 * 0.587 + 250 * 0.114 => 80)
  // and then all three RGB values would become 80 or (80, 80, 80).
  // We will use truncation to cast from the floating point result 
  // to the integer grayscale value.
  //
  // Returns: updated image.
  //
  let gscaleHelper L = 
    let (r, g, b) = L
    // converting to grayscale according to given values
    let av = int((float r) * 0.299 + (float g)*0.587 + (float b)*0.114)
    av

  let rec Grayscale (width:int) 
                    (height:int) 
                    (depth:int) 
                    (image:(int*int*int) list list) = 
    match image with 
    | [] -> []
    | hd::tl -> (List.map (fun L -> (gscaleHelper L, gscaleHelper L, gscaleHelper L)) hd)::Grayscale width height depth tl


  //
  // Threshold
  //
  // Thresholding increases image separation --- dark values 
  // become darker and light values become lighter. Given a 
  // threshold value in the range 0 < threshold < color depth,
  // each RGB value is compared to see if it's > threshold.
  // If so, that RGB value is replaced by the color depth;
  // if not, that RGB value is replaced with 0. 
  //
  // Example: if threshold is 100 and depth is 255, then given 
  // a pixel (80, 120, 160), the new pixel is (0, 255, 255).
  //
  // Returns: updated image.
  //
  let thresholdHelper threshold L = 
    if L > threshold then // if rgb greater than threshold
      255
    else // if rgb not greater than threshold
      0

  let rec Threshold (width:int) 
                    (height:int)
                    (depth:int)
                    (image:(int*int*int) list list)
                    (threshold:int) = 
    match image with 
    | [] -> []
    | hd::tl -> (List.map (fun (r, g, b) -> (thresholdHelper threshold r, thresholdHelper threshold g, thresholdHelper threshold b)) hd)::Threshold width height depth tl threshold


  //
  // FlipHorizontal:
  //
  // Flips an image so that what’s on the left is now on 
  // the right, and what’s on the right is now on the left. 
  // That is, the pixel that is on the far left end of the
  // row ends up on the far right of the row, and the pixel
  // on the far right ends up on the far left. This is 
  // repeated as you move inwards toward the row's center.
  //
  // Returns: updated image.
  //
  let rec FlipHorizontal (width:int)
                         (height:int)
                         (depth:int)
                         (image:(int*int*int) list list) = 
    match image with
    | [] -> []
    | hd::tl -> image |> List.map List.rev // apply .Rev on each List element


  //
  // Edge Detection:
  //
  // Edge detection is an algorithm used in computer vision to help
  // distinguish different objects in a picture or to distinguish an
  // object in the foreground of the picture from the background.
  //
  // Edge Detection replaces each pixel in the original image with
  // a black pixel, (0, 0, 0), if the original pixel contains an 
  // "edge" in the original image.  If the original pixel does not
  // contain an edge, the pixel is replaced with a white pixel 
  // (255, 255, 255).
  //
  // An edge occurs when the color of pixel is "significantly different"
  // when compared to the color of two of its neighboring pixels. 
  // We only compare each pixel in the image with the 
  // pixel immediately to the right of it and with the pixel
  // immediately below it. If either pixel has a color difference
  // greater than a given threshold, then it is "significantly
  // different" and an edge occurs. Note that the right-most column
  // of pixels and the bottom-most column of pixels can not perform
  // this calculation so the final image contain one less column
  // and one less row than the original image.
  //
  // To calculate the "color difference" between two pixels, we
  // treat the each pixel as a point on a 3-dimensional grid and
  // we calculate the distance between the two points using the
  // 3-dimensional extension to the Pythagorean Theorem.
  // Distance between (x1, y1, z1) and (x2, y2, z2) is
  //  sqrt ( (x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2 )
  //
  // The threshold amount will need to be given, which is an 
  // integer 0 < threshold < 255.  If the color distance between
  // the original pixel either of the two neighboring pixels 
  // is greater than the threshold amount, an edge occurs and 
  // a black pixel is put in the resulting image at the location
  // of the original pixel. 
  //
  // Returns: updated image.
  //

  // helper will take the parameters of the pixels, calculates distance, compares with threshold
  //    if 0 < threshold < 255 then 

  let helper1 (h1:(int*int*int)) (h2:(int*int*int)) = 
    let (x, y, z) = h1
    let (x2, y2, z2) = h2
    // calculate the distances
    let dist = sqrt ((pown(float x - float x2) 2) + (pown(float y - float y2) 2) + (pown(float z - float z2) 2))
    dist
    
  let rec helper2 (L1:(int*int*int) list) (L2:(int*int*int) list) (threshold:int)   = 
    match L1, L2 with
    | [], [] -> L1  // if both empty
    | h1::[], h2::[] -> []  // if only 1 in each
    | h1::t1, h2::t2 -> let dist1 = helper1 h1 h2
                        let dist2 = helper1 h1 (List.head t1)
                        // if color distance between original and neighboring pixels is greater than threshold
                        if (dist1 > float threshold || dist2 > float threshold) then
                          // put black pixel at location of original pixel
                          (0, 0, 0)::helper2 t1 t2 threshold
                        else
                          (255, 255, 255)::helper2 t1 t2 threshold

  let rec EdgeDetect (width:int)
               (height:int)
               (depth:int)
               (image:(int*int*int) list list)
               (threshold:int) = 
    match image with
    | [] -> image
    | h1::[] -> []
    | h1::n::tl -> (helper2 h1 n threshold)::(EdgeDetect width height depth (n::tl) threshold)


  //
  // RotateRight90:
  //
  // Rotates the image to the right 90 degrees.
  //
  // Returns: updated image.
  //
  let rec RotateRight90 (width:int)
                        (height:int)
                        (depth:int)
                        (image:(int*int*int) list list) = 
    // flip image horizontally, then transpose it
    FlipHorizontal width height depth (List.transpose image)

