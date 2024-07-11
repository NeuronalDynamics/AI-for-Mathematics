import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset

/- Supply proofs for 2 out of the 3 assignments.
   Do all 3 for 5 points of extra credit.

   All assignments can be proven through induction and appropriate use of library functions and logic operations.
-/

-- Assignment 1: Show that 2^n % 7 = 1, 2, or 4 for all n.
theorem assignment1 : ∀ n:ℕ, 2^n % 7 = 1 ∨ 2^n % 7 = 2 ∨ 2^n % 7 = 4 := by
  intro n
  induction n with
  | zero =>
    -- Base case: 2^0 % 7 = 1 % 7 = 1
    left
    exact Nat.mod_eq_of_lt (by norm_num)
  | succ n ih =>
    -- Inductive step: assume 2^n % 7 = 1 ∨ 2^n % 7 = 2 ∨ 2^n % 7 = 4
    cases ih with
    | inl h1 =>
      -- Case 2^n % 7 = 1: 2^(n+1) % 7 = (2 * 2^n) % 7 = (2 * 1) % 7 = 2
      right
      left
      rw [Nat.pow_succ]
      rw [Nat.mul_mod]
      rw [h1]
    | inr ih' =>
      cases ih' with
      | inl h2 =>
        -- Case 2^n % 7 = 2: 2^(n+1) % 7 = (2 * 2^n) % 7 = (2 * 2) % 7 = 4
        right
        right
        rw [Nat.pow_succ]
        rw [Nat.mul_mod]
        rw [h2]
      | inr h4 =>
        -- Case 2^n % 7 = 4: 2^(n+1) % 7 = (2 * 2^n) % 7 = (2 * 4) % 7 = 8 % 7 = 1
        left
        rw [Nat.pow_succ]
        rw [Nat.mul_mod]
        rw [h4]

-- Assignment 2: Show that (1-x)*(1+x+x^2+...+x^{n-1}) = (1-x^n)
theorem assignment2
    (x:ℝ)
    : ∀ n:ℕ, (1-x)*(∑ i ∈ Finset.range n, x^i) = 1-x^n := by
  intro n
  induction n with
  | zero =>
    -- Base case: (1-x)*(∑ i ∈ Finset.range 0, x^i) = (1-x)*0 = 0 = 1-x^0
    simp
  | succ n ih =>
    -- Inductive step: assume (1-x)*(∑ i ∈ Finset.range n, x^i) = 1-x^n
    -- (1-x)*(∑ i ∈ Finset.range (n+1), x^i) = (1-x)*(∑ i ∈ Finset.range n, x^i) + x^n
    rw [Finset.sum_range_succ]
    -- Expand and apply the inductive hypothesis
    rw [mul_add]
    rw [ih]
    -- Simplify
    rw [pow_succ]
    ring

-- Assignment 3: Show that if a_0 = 0, a_{n+1} = 2*a_n+1 then a_n = 2^n-1.
theorem assignment3
    (a: ℕ → ℝ) (h_zero: a 0 = 0) (h_rec: ∀ n:ℕ, a (n+1) = 2 * (a n) + 1)
    : ∀ n:ℕ, a n = 2^n - 1 := by
  intro n
  induction n with
  | zero =>
    -- Base case: a 0 = 0 = 2^0 - 1
    simp [h_zero]
  | succ n ih =>
    -- Inductive step: assume a n = 2^n - 1
    -- a (n+1) = 2 * a n + 1 = 2 * (2^n - 1) + 1 = 2^(n+1) - 2 + 1 = 2^(n+1) - 1
    rw [h_rec]
    rw [ih]
    ring
