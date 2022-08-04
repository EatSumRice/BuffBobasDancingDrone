
(cl:in-package :asdf)

(defsystem "buff_boba_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Song" :depends-on ("_package_Song"))
    (:file "_package_Song" :depends-on ("_package"))
    (:file "moves" :depends-on ("_package_moves"))
    (:file "_package_moves" :depends-on ("_package"))
    (:file "numbermoves" :depends-on ("_package_numbermoves"))
    (:file "_package_numbermoves" :depends-on ("_package"))
  ))