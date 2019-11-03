module HW5Part1 where

-- I understand that my submission is very late but the thing is I didnot understand how to do this assignment
-- I hadn't gone through the slides and StackLang.hs file before so I was stuck as in my previous submission
-- I could finally understand the solution today and I tried to write things on my own, to prepare for the quiz  

data Reg
  = A
  | B
  deriving (Eq,Show)

data Expr
  = LitI Int
  | LitB Bool  
  | Get Reg 
  | Add Expr Expr
  | LessThanOrEqualTo Expr Expr
  | Negation Expr
  | Conjuction Expr Expr
  deriving (Eq,Show)

data Stmt
  = Set Reg Expr
  | Conditional Expr Prog Prog 
  deriving (Eq,Show)

type Prog = [ Stmt ]
given_program = [
  (Set A (LitI 3)),
  (Set B (Add (Get A) (LitI 2))),
  (Conditional (LessThanOrEqualTo (Get A) (Get B)) [(Set A (Add (Get A) (Get A)))] [(Set B (Add (Get B) (Get B)))]),
  (Set B (Add (Get A) (Get B)))]

sumFiveOrLess :: [Int] -> Prog
sumFiveOrLess x = Set A (LitI 0) : map func x
  where
    func elem = Conditional (LessThanOrEqualTo (LitI elem) (LitI 5)) [(Set A (Add (Get A) (LitI elem)))] []

