// Generated by gencpp from file buff_boba_pkg/numbermoves.msg
// DO NOT EDIT!


#ifndef BUFF_BOBA_PKG_MESSAGE_NUMBERMOVES_H
#define BUFF_BOBA_PKG_MESSAGE_NUMBERMOVES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace buff_boba_pkg
{
template <class ContainerAllocator>
struct numbermoves_
{
  typedef numbermoves_<ContainerAllocator> Type;

  numbermoves_()
    : number(0)  {
    }
  numbermoves_(const ContainerAllocator& _alloc)
    : number(0)  {
  (void)_alloc;
    }



   typedef int32_t _number_type;
  _number_type number;





  typedef boost::shared_ptr< ::buff_boba_pkg::numbermoves_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::buff_boba_pkg::numbermoves_<ContainerAllocator> const> ConstPtr;

}; // struct numbermoves_

typedef ::buff_boba_pkg::numbermoves_<std::allocator<void> > numbermoves;

typedef boost::shared_ptr< ::buff_boba_pkg::numbermoves > numbermovesPtr;
typedef boost::shared_ptr< ::buff_boba_pkg::numbermoves const> numbermovesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::buff_boba_pkg::numbermoves_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::buff_boba_pkg::numbermoves_<ContainerAllocator1> & lhs, const ::buff_boba_pkg::numbermoves_<ContainerAllocator2> & rhs)
{
  return lhs.number == rhs.number;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::buff_boba_pkg::numbermoves_<ContainerAllocator1> & lhs, const ::buff_boba_pkg::numbermoves_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace buff_boba_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::buff_boba_pkg::numbermoves_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::buff_boba_pkg::numbermoves_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::buff_boba_pkg::numbermoves_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2474488a3908093ec1307bdd5b35815e";
  }

  static const char* value(const ::buff_boba_pkg::numbermoves_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2474488a3908093eULL;
  static const uint64_t static_value2 = 0xc1307bdd5b35815eULL;
};

template<class ContainerAllocator>
struct DataType< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "buff_boba_pkg/numbermoves";
  }

  static const char* value(const ::buff_boba_pkg::numbermoves_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 number\n"
;
  }

  static const char* value(const ::buff_boba_pkg::numbermoves_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.number);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct numbermoves_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::buff_boba_pkg::numbermoves_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::buff_boba_pkg::numbermoves_<ContainerAllocator>& v)
  {
    s << indent << "number: ";
    Printer<int32_t>::stream(s, indent + "  ", v.number);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BUFF_BOBA_PKG_MESSAGE_NUMBERMOVES_H