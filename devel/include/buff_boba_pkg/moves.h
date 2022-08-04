// Generated by gencpp from file buff_boba_pkg/moves.msg
// DO NOT EDIT!


#ifndef BUFF_BOBA_PKG_MESSAGE_MOVES_H
#define BUFF_BOBA_PKG_MESSAGE_MOVES_H


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
struct moves_
{
  typedef moves_<ContainerAllocator> Type;

  moves_()
    : moveList()  {
    }
  moves_(const ContainerAllocator& _alloc)
    : moveList(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _moveList_type;
  _moveList_type moveList;





  typedef boost::shared_ptr< ::buff_boba_pkg::moves_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::buff_boba_pkg::moves_<ContainerAllocator> const> ConstPtr;

}; // struct moves_

typedef ::buff_boba_pkg::moves_<std::allocator<void> > moves;

typedef boost::shared_ptr< ::buff_boba_pkg::moves > movesPtr;
typedef boost::shared_ptr< ::buff_boba_pkg::moves const> movesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::buff_boba_pkg::moves_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::buff_boba_pkg::moves_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::buff_boba_pkg::moves_<ContainerAllocator1> & lhs, const ::buff_boba_pkg::moves_<ContainerAllocator2> & rhs)
{
  return lhs.moveList == rhs.moveList;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::buff_boba_pkg::moves_<ContainerAllocator1> & lhs, const ::buff_boba_pkg::moves_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace buff_boba_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::buff_boba_pkg::moves_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::buff_boba_pkg::moves_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::buff_boba_pkg::moves_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::buff_boba_pkg::moves_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::buff_boba_pkg::moves_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::buff_boba_pkg::moves_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::buff_boba_pkg::moves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4697aa5897206b11660bd043405f4a49";
  }

  static const char* value(const ::buff_boba_pkg::moves_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4697aa5897206b11ULL;
  static const uint64_t static_value2 = 0x660bd043405f4a49ULL;
};

template<class ContainerAllocator>
struct DataType< ::buff_boba_pkg::moves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "buff_boba_pkg/moves";
  }

  static const char* value(const ::buff_boba_pkg::moves_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::buff_boba_pkg::moves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string moveList\n"
;
  }

  static const char* value(const ::buff_boba_pkg::moves_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::buff_boba_pkg::moves_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.moveList);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct moves_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::buff_boba_pkg::moves_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::buff_boba_pkg::moves_<ContainerAllocator>& v)
  {
    s << indent << "moveList: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.moveList);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BUFF_BOBA_PKG_MESSAGE_MOVES_H