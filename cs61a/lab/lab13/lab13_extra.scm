; Lab 13: Final Review - Optional Questions

; Q6
(define (nodots s)
  (cond ((null? s) s)
        ((pair? (car s)) (cond ((number? (cdr s)) (cons (nodots (car s)) (cons (cdr s) nil)))
                               (else (cons (nodots (car s)) (nodots (cdr s))))))
        (else (if (number? (cdr s)) (cons (car s) (cons (cdr s) nil))
                                    (cons (car s) (nodots (cdr s)))))
))

; Q7
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          (else (pair-tracker (cons-stream curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)
1
(define (contains? lst s)
  (if (null? lst)
    #f
    (if (eq? (car lst) s)
        #t
        (contains? (cdr-stream lst
        ) s)))
)

; Q8
(define-macro (switch expr cases)
    (cons 'begin (map (lambda (case) (if (equal? (eval expr) (car case)) (car (cdr case)))) cases))
)
