//
// Parser for simple C programs.  This component checks 
// the input program to see if it meets the syntax rules
// of simple C.  The parser returns a string denoting
// success or failure. 
//
// Returns: the string "success" if the input program is
// legal, otherwise the string "syntax_error: ..." is
// returned denoting an invalid simple C program.
//
// Harsh Dasika
//
// Original author:
//   Prof. Joe Hummel
//   U. of Illinois, Chicago
//   CS 341, Spring 2022
//

namespace compiler

module parser =
  //
  // NOTE: all functions in the module must be indented.
  //

  //
  // matchToken
  //
  let private matchToken expected_token (tokens : string List) =
    //
    // if the next token matches the expected token,  
    // keep parsing by returning the rest of the tokens.
    // Otherwise throw an exception because there's a 
    // syntax error, effectively stopping compilation
    // at the first error.
    //
    let next_token = List.head tokens

    if expected_token = next_token then  
      List.tail tokens
    elif next_token.StartsWith(expected_token) then
      List.tail tokens
    else
      failwith ("expecting " + expected_token + ", but found " + next_token)

  // empty: for semicolons
  let rec empty tokens = 
    let T2 = matchToken ";" tokens
    T2

  // vardecl: for declaring an int variable
  let rec vardecl tokens = 
    let T2 = matchToken "int" tokens
    let T3 = matchToken "identifier" T2
    let T4 = matchToken ";" T3
    T4

  // input: for cin statements
  let rec input tokens = 
    let T2 = matchToken "cin" tokens
    let T3 = matchToken ">>" T2
    let T4 = matchToken "identifier" T3
    let T5 = matchToken ";" T4
    T5

  // expr_value: for things used in comparison expressions
  let rec expr_value (tokens : string List) = 
    let next_token = List.head tokens
    if next_token.StartsWith("identifier") then
      let T2 = matchToken "identifier" tokens
      T2
    elif next_token.StartsWith("int_literal") then
      let T2 = matchToken "int_literal" tokens
      T2
    elif next_token.StartsWith("str_literal") then
      let T2 = matchToken "str_literal" tokens
      T2
    elif next_token = "true" then
      let T2 = matchToken "true" tokens
      T2
    elif next_token = "false" then
      let T2 = matchToken "false" tokens
      T2
    else
      // not found
      failwith ("expecting identifier or literal, but found " + next_token)

  // output_value: for checking endl and if expr-value exists
  let rec output_value tokens = 
    let next_token = List.head tokens
    // if only endl
    if next_token = "endl" then
      let T2 = matchToken "endl" tokens
      T2
    else
      // if expr-value is there
      let T2 = expr_value tokens
      T2

  // output: for returning the cout statements
  let rec output tokens = 
    let T2 = matchToken "cout" tokens
    let T3 = matchToken "<<" T2
    let T4 = output_value T3
    let T5 = matchToken ";" T4
    T5

  // expr_op: to select the operations for the if/else's
  let rec expr_op tokens = 
    let next_token = List.head tokens
    if next_token = "+" ||
      next_token = "-" ||
      next_token = "*" ||
      next_token = "/" ||
      next_token = "^" ||
      next_token = "<" ||
      next_token = "<=" ||
      next_token = ">" ||
      next_token = ">=" ||
      next_token = "==" ||
      next_token = "!=" then
      let T2 = matchToken next_token tokens
      T2
    else
      // if none found in the expression
      failwith ("expecting expression operator, but found " + next_token)

  // expr: to form the complete expression or just the independent expr-value
  let rec expr tokens = 
    let T2 = expr_value tokens
    let next_token = List.head T2
    if next_token = "+" ||
      next_token = "-" ||
      next_token = "*" ||
      next_token = "/" ||
      next_token = "^" ||
      next_token = "<" ||
      next_token = "<=" ||
      next_token = ">" ||
      next_token = ">=" ||
      next_token = "==" ||
      next_token = "!=" then
      let T3 = expr_op T2
      let T4 = expr_value T3
      T4
    else
      // no operators after T2
      T2

  // assignment: for variable assignments (e.g. x = 5)
  let rec assignment tokens = 
    let T2 = matchToken "identifier" tokens
    let T3 = matchToken "=" T2
    let T4 = expr T3
    let T5 = matchToken ";" T4
    T5

  // stmt: for figuring out what type of statement to look for
  let rec private stmt tokens = 
    let next_token = List.head tokens
    if next_token = ";" then
      let T2 = empty tokens
      T2
    elif next_token = "int" then
      let T2 = vardecl tokens
      T2
    elif next_token = "cin" then
      let T2 = input tokens
      T2
    elif next_token = "cout" then
      let T2 = output tokens
      T2
    elif next_token.StartsWith("identifier") then
      let T2 = assignment tokens
      T2
    elif next_token = "if" then
      let T2 = ifstmt tokens
      T2
    else 
      // if no statement found at all
      failwith ("expecting statement, but found " + next_token)

  // ifstmt: for if-statements and expressions
  and private ifstmt tokens =
    let T2 = matchToken "if" tokens
    let T3 = matchToken "(" T2
    let T4 = condition T3
    let T5 = matchToken ")" T4
    let T6 = then_part T5
    let T7 = else_part T6
    T7
  // condition: for the conditions in the if-else's
  and private condition tokens = 
    let T2 = expr tokens
    T2
  // then_part: for "if blah blah blah THEN do..."
  and private then_part tokens =
    let T2 = stmt tokens
    T2
  // else_part: for "else, do this..."
  and private else_part tokens =
    let next_token = List.head tokens
    if next_token = "else" then
      let T2 = matchToken "else" tokens
      let T3 = stmt T2
      T3
    else
      tokens

  // morestmts: if there is more than 1 stmt, need to call this over and over until none left
  let rec private morestmts tokens = 
    let next_token = List.head tokens
    if next_token = ";" ||
      next_token = "int" ||
      next_token = "cin" ||
      next_token = "cout" ||
      next_token = "int" ||
      next_token.StartsWith("identifier") ||
      next_token = "if" then
      let T2 = stmt tokens
      let T3 = morestmts T2
      T3
    else 
      // if there aren't any more statements
      tokens

  // stmts: if there is only 1 statement or to check if morestmts is needed
  let rec private stmts tokens = 
    let T2 = stmt tokens
    let T3 = morestmts T2
    T3

  // simpleC
  let private simpleC tokens = 
    let T2 = matchToken "void" tokens
    let T3 = matchToken "main" T2
    let T4 = matchToken "(" T3
    let T5 = matchToken ")" T4
    let T6 = matchToken "{" T5
    let T7 = stmts T6
    let T8 = matchToken "}" T7
    let T9 = matchToken "$" T8
    T9
    

  //
  // parse tokens
  //
  // Given a list of tokens, parses the list and determines
  // if the list represents a valid simple C program.  Returns
  // the string "success" if valid, otherwise returns a 
  // string of the form "syntax_error:...".
  //
  let parse tokens = 
    try
      let result = simpleC tokens
      "success"
    with 
      | ex -> "syntax_error: " + ex.Message
