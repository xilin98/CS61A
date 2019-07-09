;; Extra Scheme Questions ;;


; Q5
(define lst
  (list (list 1) 2 (cons 3 4) 5)
)

; Q6
(define (composed f g)
  'YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  'YOUR-CODE-HERE
  (filter (lambda (x) (not (= item x))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (no-repeats s)
  'YOUR-CODE-HERE
  (if (null? s)
    s
    (cons (car s) (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s))))
  )
)

; Q9
(define (substitute s old new)
  'YOUR-CODE-HERE
  (if (null? s)
    s
    (if (pair? (car s))
      (cons (substitute (car s) old new) (substitute (cdr s) old new))
      (if (eq? (car s) old)
        (cons new (substitute (cdr s) old new))
        (cons (car s) (substitute (cdr s) old new))
      )
    )
  )
)

; Q10
(define (sub-all s olds news)
  'YOUR-CODE-HERE
  (if (null? olds)
    s
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
  )
)
