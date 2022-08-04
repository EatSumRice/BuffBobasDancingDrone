// Generated by gencpp from file buff_pkg/Moves.msg
// DO NOT EDIT!


#ifndef BUFF_PKG_MESSAGE_MOVES_H
#define BUFF_PKG_MESSAGE_MOVES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace buff_pkg
{
template <class ContainerAllocator>
struct Moves_
{
  typedef Moves_<ContainerAllocator> Type;

  Moves_()
    : moveList()  {
    }
  Moves_(const ContainerAllocator& _alloc)
    : moveList(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _moveList_type;
  _moveList_type moveList;





  typedef boost::shared_ptr< ::buff_pkg::Moves_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::buff_pkg::Moves_<ContainerAllocator> const> ConstPtr;

}; // struct Moves_

typedef ::buff_pkg::Moves_<std::allocator<void> > Moves;

typedef boost::shared_ptr< ::buff_pkg::Moves > MovesPtr;
typedef boost::shared_ptr< ::buff_pkg::Moves const> MovesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::buff_pkg::Moves_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::buff_pkg::Moves_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::buff_pkg::Moves_<ContainerAllocator1> & lhs, const ::buff_pkg::Moves_<ContainerAllocator2> & rhs)
{
  return lhs.moveList == rhs.moveList;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::buff_pkg::Moves_<ContainerAllocator1> & lhs, const ::buff_pkg::Moves_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace buff_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::buff_pkg::Moves_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::buff_pkg::Moves_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::buff_pkg::Moves_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::buff_pkg::Moves_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::buff_pkg::Moves_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::buff_pkg::Moves_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::buff_pkg::Moves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4697aa5897206b11660bd043405f4a49";
  }

  static const char* value(const ::buff_pkg::Moves_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4697aa5897206b11ULL;
  static const uint64_t static_value2 = 0x660bd043405f4a49ULL;
};

template<class ContainerAllocator>
struct DataType< ::buff_pkg::Moves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "buff_pkg/Moves";
  }

  static const char* value(const ::buff_pkg::Moves_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::buff_pkg::Moves_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string moveList\n"
;
  }

  static const char* value(const ::buff_pkg::Moves_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::buff_pkg::Moves_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.moveList);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Moves_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::buff_pkg::Moves_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::buff_pkg::Moves_<ContainerAllocator>& v)
  {
    s << indent << "moveList: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.moveList);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BUFF_PKG_MESSAGE_MOVES_H