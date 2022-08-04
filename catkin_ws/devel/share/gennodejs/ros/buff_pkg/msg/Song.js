// Auto-generated. Do not edit!

// (in-package buff_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Song {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.filename = null;
      this.tempo = null;
      this.time_sig = null;
      this.pickup = null;
      this.beat_durations = null;
    }
    else {
      if (initObj.hasOwnProperty('filename')) {
        this.filename = initObj.filename
      }
      else {
        this.filename = '';
      }
      if (initObj.hasOwnProperty('tempo')) {
        this.tempo = initObj.tempo
      }
      else {
        this.tempo = 0.0;
      }
      if (initObj.hasOwnProperty('time_sig')) {
        this.time_sig = initObj.time_sig
      }
      else {
        this.time_sig = 0;
      }
      if (initObj.hasOwnProperty('pickup')) {
        this.pickup = initObj.pickup
      }
      else {
        this.pickup = false;
      }
      if (initObj.hasOwnProperty('beat_durations')) {
        this.beat_durations = initObj.beat_durations
      }
      else {
        this.beat_durations = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Song
    // Serialize message field [filename]
    bufferOffset = _serializer.string(obj.filename, buffer, bufferOffset);
    // Serialize message field [tempo]
    bufferOffset = _serializer.float32(obj.tempo, buffer, bufferOffset);
    // Serialize message field [time_sig]
    bufferOffset = _serializer.int32(obj.time_sig, buffer, bufferOffset);
    // Serialize message field [pickup]
    bufferOffset = _serializer.bool(obj.pickup, buffer, bufferOffset);
    // Serialize message field [beat_durations]
    bufferOffset = _arraySerializer.float32(obj.beat_durations, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Song
    let len;
    let data = new Song(null);
    // Deserialize message field [filename]
    data.filename = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [tempo]
    data.tempo = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [time_sig]
    data.time_sig = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [pickup]
    data.pickup = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [beat_durations]
    data.beat_durations = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.filename);
    length += 4 * object.beat_durations.length;
    return length + 17;
  }

  static datatype() {
    // Returns string type for a message object
    return 'buff_pkg/Song';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9b8923dbcfe00245bdb812b481eeb694';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string filename
    float32 tempo
    int32 time_sig
    bool pickup
    float32[] beat_durations
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Song(null);
    if (msg.filename !== undefined) {
      resolved.filename = msg.filename;
    }
    else {
      resolved.filename = ''
    }

    if (msg.tempo !== undefined) {
      resolved.tempo = msg.tempo;
    }
    else {
      resolved.tempo = 0.0
    }

    if (msg.time_sig !== undefined) {
      resolved.time_sig = msg.time_sig;
    }
    else {
      resolved.time_sig = 0
    }

    if (msg.pickup !== undefined) {
      resolved.pickup = msg.pickup;
    }
    else {
      resolved.pickup = false
    }

    if (msg.beat_durations !== undefined) {
      resolved.beat_durations = msg.beat_durations;
    }
    else {
      resolved.beat_durations = []
    }

    return resolved;
    }
};

module.exports = Song;
