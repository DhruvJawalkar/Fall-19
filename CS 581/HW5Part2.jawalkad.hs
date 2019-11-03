module HW5Part2 where

-- 
-- We separate bool type and int type operations by using a different data type
-- int ::= (any integer)
-- bool ::= true | false
-- reg  ::= A | B

-- expr ::= int
--       |  reg
--       |  expr + expr
-- 
-- boolexptype ::= bool
--              |  expr <= expr
--              |  not boolexptype
--              |  boolexptype & boolexptype
--
-- stmt ::= reg := expr
--       |  if boolexptype then prog else prog end

-- prog ::= e (Null)
--       | stmt
--       | prog

data Reg
  = A
  | B
  deriving (Eq,Show)

data Expr
  = LitI Int 
  | Get Reg 
  | Add Expr Expr
  deriving (Eq,Show)

data BoolExpType
  = LitB Bool
  | LessThanOrEqualTo Expr Expr
  | Negation BoolExpType
  | Conjuction BoolExpType BoolExpType
  deriving (Eq,Show)

data Stmt
  = Set Reg Expr
  | Conditional BoolExpType Prog Prog 
  deriving (Eq,Show)

type Prog = [ Stmt ]
