; Auto-generated. Do not edit!


(cl:in-package buff_pkg-msg)


;//! \htmlinclude Song.msg.html

(cl:defclass <Song> (roslisp-msg-protocol:ros-message)
  ((filename
    :reader filename
    :initarg :filename
    :type cl:string
    :initform "")
   (tempo
    :reader tempo
    :initarg :tempo
    :type cl:float
    :initform 0.0)
   (time_sig
    :reader time_sig
    :initarg :time_sig
    :type cl:integer
    :initform 0)
   (pickup
    :reader pickup
    :initarg :pickup
    :type cl:boolean
    :initform cl:nil)
   (beat_durations
    :reader beat_durations
    :initarg :beat_durations
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Song (<Song>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Song>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Song)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name buff_pkg-msg:<Song> is deprecated: use buff_pkg-msg:Song instead.")))

(cl:ensure-generic-function 'filename-val :lambda-list '(m))
(cl:defmethod filename-val ((m <Song>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader buff_pkg-msg:filename-val is deprecated.  Use buff_pkg-msg:filename instead.")
  (filename m))

(cl:ensure-generic-function 'tempo-val :lambda-list '(m))
(cl:defmethod tempo-val ((m <Song>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader buff_pkg-msg:tempo-val is deprecated.  Use buff_pkg-msg:tempo instead.")
  (tempo m))

(cl:ensure-generic-function 'time_sig-val :lambda-list '(m))
(cl:defmethod time_sig-val ((m <Song>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader buff_pkg-msg:time_sig-val is deprecated.  Use buff_pkg-msg:time_sig instead.")
  (time_sig m))

(cl:ensure-generic-function 'pickup-val :lambda-list '(m))
(cl:defmethod pickup-val ((m <Song>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader buff_pkg-msg:pickup-val is deprecated.  Use buff_pkg-msg:pickup instead.")
  (pickup m))

(cl:ensure-generic-function 'beat_durations-val :lambda-list '(m))
(cl:defmethod beat_durations-val ((m <Song>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader buff_pkg-msg:beat_durations-val is deprecated.  Use buff_pkg-msg:beat_durations instead.")
  (beat_durations m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Song>) ostream)
  "Serializes a message object of type '<Song>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'filename))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'filename))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'tempo))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'time_sig)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'pickup) 1 0)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'beat_durations))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'beat_durations))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Song>) istream)
  "Deserializes a message object of type '<Song>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'filename) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'filename) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'tempo) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'time_sig) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:slot-value msg 'pickup) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'beat_durations) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'beat_durations)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Song>)))
  "Returns string type for a message object of type '<Song>"
  "buff_pkg/Song")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Song)))
  "Returns string type for a message object of type 'Song"
  "buff_pkg/Song")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Song>)))
  "Returns md5sum for a message object of type '<Song>"
  "9b8923dbcfe00245bdb812b481eeb694")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Song)))
  "Returns md5sum for a message object of type 'Song"
  "9b8923dbcfe00245bdb812b481eeb694")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Song>)))
  "Returns full string definition for message of type '<Song>"
  (cl:format cl:nil "string filename~%float32 tempo~%int32 time_sig~%bool pickup~%float32[] beat_durations~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Song)))
  "Returns full string definition for message of type 'Song"
  (cl:format cl:nil "string filename~%float32 tempo~%int32 time_sig~%bool pickup~%float32[] beat_durations~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Song>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'filename))
     4
     4
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'beat_durations) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Song>))
  "Converts a ROS message object to a list"
  (cl:list 'Song
    (cl:cons ':filename (filename msg))
    (cl:cons ':tempo (tempo msg))
    (cl:cons ':time_sig (time_sig msg))
    (cl:cons ':pickup (pickup msg))
    (cl:cons ':beat_durations (beat_durations msg))
))
