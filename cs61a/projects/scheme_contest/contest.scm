;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: LIGHT IN NIGHT
;;;
;;; Description:
;;;   <Dark is coming but
;;;    You will see
;;;    the little things in the sky>
(define (draw)
  (define colored
      (cons-stream "red" (cons-stream "yellow" (cons-stream "blue" (cons-stream "green" (cons-stream "purple"  (cons-stream "yellow" colored)))))))

  (define (bigcircle r cl angle)
    (color (car cl))
    (begin_fill)
    (circle r)
    (end_fill)
    (lt angle)
    (if (< r 0) (circle r) (bigcircle (- r 0.5) (cdr-stream cl) angle)))

  (define (star num size angle cl)
    (color (car cl))
    (setposition 0 0)
    (pendown)
    (fd size)
    (lt angle)
    (bk size)
    (if (< num 0) (circle 0) (star (- num 1) size angle (cdr-stream cl))))

  (bgcolor "black")
  ;(star 750 1000 0.5 colored)
  (bigcircle 150  colored 215)
)

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
