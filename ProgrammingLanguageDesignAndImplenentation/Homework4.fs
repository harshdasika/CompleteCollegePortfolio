//
// F# program to input a string and print out information
// about the # of vowels and digraphs in that string.
//
// Name: Harsh Dasika
//
// Original author:
//   Prof. Joe Hummel
//   U. of Illinois, Chicago
//   CS 341, Spring 2022
//

//
// explode:
//
// Given a string s, explodes the string into a list of characters.
// Example: explode "apple" => ['a';'p';'p';'l';'e']
//
let explode (S:string) = 
  List.ofArray (S.ToCharArray())

//
// implode
//
// The opposite of explode --- given a list of characters, returns
// the list as a string. Example: implode ['t';'h';'e'] => "the"
//
let implode (L:char list) = 
  new string(List.toArray L)

let rec length L = 
  match L with
  | []     -> 0   (*if empty*)
  | hd::tl -> 1 + length tl  (*add 1 if exists*)
  | _::tl  -> 0 + length tl

let rec count v L = 
  match L with
  | []                 -> 0
  | hd::tl when hd = v -> 1 + count v tl
  | _ ::tl             -> 0 + count v tl

let rec numVowels L = 
  let counts = List.map (fun v -> count v L) ['a';'e';'i';'o';'u']
  List.sum counts


let rec countDigraph c_1 c_2 L = 
  match L with
  | []                  -> 0
  | hd::next::tl when hd = c_1 && next = c_2 -> 1 + countDigraph c_1 c_2 (c_2::tl)
  | _::tl               -> 0 + countDigraph c_1 c_2 tl

let printCountDigraph L (c1, c2) =
  printfn "%A,%A: %A" c1 c2 (countDigraph c1 c2 L)




[<EntryPoint>]
let main argv =
  printfn "Starting"
  printfn ""

  //
  // input string, output length and # of vowels:
  //
  printf("input> ")
  let input = System.Console.ReadLine()

  let L = explode input
  printfn "exploded: %A" L

  let len = length L
  printfn "length: %A" len

  let num = numVowels L
  printfn "vowels: %A" num

  //
  // TODO: print count of each vowel:
  //
  printfn "%A: %A" 'a' (count 'a' L)
  printfn "%A: %A" 'e' (count 'e' L)
  printfn "%A: %A" 'i' (count 'i' L)
  printfn "%A: %A" 'o' (count 'o' L)
  printfn "%A: %A" 'u' (count 'u' L)
  
  //
  // TODO: print number of digraphs, count of each:
  //
  let chars = [('a','i'); ('c','h'); ('e','a'); ('i','e'); ('o','u'); ('p','h'); ('s','h'); ('t','h'); ('w','h')]

  let list = (countDigraph 'a' 'i' L) + (countDigraph 'c' 'h' L) + 
             (countDigraph 'e' 'a' L) + (countDigraph 'i' 'e' L) + 
             (countDigraph 'o' 'u' L) + (countDigraph 'p' 'h' L) + 
             (countDigraph 's' 'h' L) + (countDigraph 't' 'h' L) + 
             (countDigraph 'w' 'h' L)
  printfn "digraphs: %A" list

  List.iter (fun x -> printCountDigraph L x) chars

  //
  // done: implode list, print, and return
  //
  let S = implode L
  printfn "imploded: %A" S

  printfn ""
  printfn "Done"
  0  // return 0 => success, much like C++