
(cl:in-package :asdf)

(defsystem "buff_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Song" :depends-on ("_package_Song"))
    (:file "_package_Song" :depends-on ("_package"))
  ))