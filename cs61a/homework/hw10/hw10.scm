(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term)))
)

(define (accumulate-tail combiner start n term)
  (if (= n 0)
    start
    (accumulate-tail combiner (combiner (term n) start) (- n 1) term))
)

(define (partial-sums stream)
  (define (helper so-far stream)
    (if (null? stream)
      nil
      (cons-stream (+ so-far (car stream)) (helper (+ so-far (car stream)) (cdr-stream stream)))))
  (helper 0 stream)
)


(define (rle s)
  (define (helper elem num s)
    (cond
      ((null? (cdr-stream s)) (cons-stream (list elem num) nil))
      ((= elem (car (cdr-stream s))) (helper elem (+ num 1) (cdr-stream s)))
      (else (cons-stream (list elem num) (helper (car (cdr-stream s)) 1 (cdr-stream s))))))
  (if (null? s)
      nil
      (helper (car s) 1 s))
)
