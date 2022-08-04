;; Auto-generated. Do not edit!


(when (boundp 'buff_boba_pkg::moves)
  (if (not (find-package "BUFF_BOBA_PKG"))
    (make-package "BUFF_BOBA_PKG"))
  (shadow 'moves (find-package "BUFF_BOBA_PKG")))
(unless (find-package "BUFF_BOBA_PKG::MOVES")
  (make-package "BUFF_BOBA_PKG::MOVES"))

(in-package "ROS")
;;//! \htmlinclude moves.msg.html


(defclass buff_boba_pkg::moves
  :super ros::object
  :slots (_moveList ))

(defmethod buff_boba_pkg::moves
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

(setf (get buff_boba_pkg::moves :md5sum-) "4697aa5897206b11660bd043405f4a49")
(setf (get buff_boba_pkg::moves :datatype-) "buff_boba_pkg/moves")
(setf (get buff_boba_pkg::moves :definition-)
      "string moveList
")



(provide :buff_boba_pkg/moves "4697aa5897206b11660bd043405f4a49")


