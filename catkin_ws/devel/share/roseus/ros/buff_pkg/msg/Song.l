;; Auto-generated. Do not edit!


(when (boundp 'buff_pkg::Song)
  (if (not (find-package "BUFF_PKG"))
    (make-package "BUFF_PKG"))
  (shadow 'Song (find-package "BUFF_PKG")))
(unless (find-package "BUFF_PKG::SONG")
  (make-package "BUFF_PKG::SONG"))

(in-package "ROS")
;;//! \htmlinclude Song.msg.html


(defclass buff_pkg::Song
  :super ros::object
  :slots (_filename _tempo _time_sig _pickup _beat_durations ))

(defmethod buff_pkg::Song
  (:init
   (&key
    ((:filename __filename) "")
    ((:tempo __tempo) 0.0)
    ((:time_sig __time_sig) 0)
    ((:pickup __pickup) nil)
    ((:beat_durations __beat_durations) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _filename (string __filename))
   (setq _tempo (float __tempo))
   (setq _time_sig (round __time_sig))
   (setq _pickup __pickup)
   (setq _beat_durations __beat_durations)
   self)
  (:filename
   (&optional __filename)
   (if __filename (setq _filename __filename)) _filename)
  (:tempo
   (&optional __tempo)
   (if __tempo (setq _tempo __tempo)) _tempo)
  (:time_sig
   (&optional __time_sig)
   (if __time_sig (setq _time_sig __time_sig)) _time_sig)
  (:pickup
   (&optional (__pickup :null))
   (if (not (eq __pickup :null)) (setq _pickup __pickup)) _pickup)
  (:beat_durations
   (&optional __beat_durations)
   (if __beat_durations (setq _beat_durations __beat_durations)) _beat_durations)
  (:serialization-length
   ()
   (+
    ;; string _filename
    4 (length _filename)
    ;; float32 _tempo
    4
    ;; int32 _time_sig
    4
    ;; bool _pickup
    1
    ;; float32[] _beat_durations
    (* 4    (length _beat_durations)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _filename
       (write-long (length _filename) s) (princ _filename s)
     ;; float32 _tempo
       (sys::poke _tempo (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _time_sig
       (write-long _time_sig s)
     ;; bool _pickup
       (if _pickup (write-byte -1 s) (write-byte 0 s))
     ;; float32[] _beat_durations
     (write-long (length _beat_durations) s)
     (dotimes (i (length _beat_durations))
       (sys::poke (elt _beat_durations i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _filename
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _filename (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _tempo
     (setq _tempo (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _time_sig
     (setq _time_sig (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _pickup
     (setq _pickup (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32[] _beat_durations
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _beat_durations (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _beat_durations i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get buff_pkg::Song :md5sum-) "9b8923dbcfe00245bdb812b481eeb694")
(setf (get buff_pkg::Song :datatype-) "buff_pkg/Song")
(setf (get buff_pkg::Song :definition-)
      "string filename
float32 tempo
int32 time_sig
bool pickup
float32[] beat_durations

")



(provide :buff_pkg/Song "9b8923dbcfe00245bdb812b481eeb694")


