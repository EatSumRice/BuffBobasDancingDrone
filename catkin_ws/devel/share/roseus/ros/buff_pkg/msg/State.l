;; Auto-generated. Do not edit!


(when (boundp 'buff_pkg::State)
  (if (not (find-package "BUFF_PKG"))
    (make-package "BUFF_PKG"))
  (shadow 'State (find-package "BUFF_PKG")))
(unless (find-package "BUFF_PKG::STATE")
  (make-package "BUFF_PKG::STATE"))

(in-package "ROS")
;;//! \htmlinclude State.msg.html


(defclass buff_pkg::State
  :super ros::object
  :slots (_number ))

(defmethod buff_pkg::State
  (:init
   (&key
    ((:number __number) 0)
    )
   (send-super :init)
   (setq _number (round __number))
   self)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:serialization-length
   ()
   (+
    ;; int32 _number
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _number
       (write-long _number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _number
     (setq _number (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get buff_pkg::State :md5sum-) "2474488a3908093ec1307bdd5b35815e")
(setf (get buff_pkg::State :datatype-) "buff_pkg/State")
(setf (get buff_pkg::State :definition-)
      "int32 number
")



(provide :buff_pkg/State "2474488a3908093ec1307bdd5b35815e")


