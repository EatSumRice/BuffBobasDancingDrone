;; Auto-generated. Do not edit!


(when (boundp 'buff_pkg::Moves)
  (if (not (find-package "BUFF_PKG"))
    (make-package "BUFF_PKG"))
  (shadow 'Moves (find-package "BUFF_PKG")))
(unless (find-package "BUFF_PKG::MOVES")
  (make-package "BUFF_PKG::MOVES"))

(in-package "ROS")
;;//! \htmlinclude Moves.msg.html


(defclass buff_pkg::Moves
  :super ros::object
  :slots (_moveList ))

(defmethod buff_pkg::Moves
  (:init
   (&key
    ((:moveList __moveList) "")
    )
   (send-super :init)
   (setq _moveList (string __moveList))
   self)
  (:moveList
   (&optional __moveList)
   (if __moveList (setq _moveList __moveList)) _moveList)
  (:serialization-length
   ()
   (+
    ;; string _moveList
    4 (length _moveList)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _moveList
       (write-long (length _moveList) s) (princ _moveList s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _moveList
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _moveList (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get buff_pkg::Moves :md5sum-) "4697aa5897206b11660bd043405f4a49")
(setf (get buff_pkg::Moves :datatype-) "buff_pkg/Moves")
(setf (get buff_pkg::Moves :definition-)
      "string moveList
")



(provide :buff_pkg/Moves "4697aa5897206b11660bd043405f4a49")


