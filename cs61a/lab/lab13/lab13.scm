; Lab 13: Final Review

; Q3
(define (compose-all funcs)
  (define (helper funcs f)
          (if (null? funcs)
              f
              (helper (cdr funcs) (lambda (x) ((car funcs) (f x))))))
  (helper funcs (lambda (x) x))
)
