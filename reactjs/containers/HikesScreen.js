import React, { Component } from 'react';
import { connect } from 'react-redux';

class HikesScreen extends Component {
  render() {
    return (
      <h2>Where are my Hikes?</h2>
    );
  }
}

// which props do we want to inject, given the global store state?
function mapStateToProps(state) {
  return {};
}

export default connect(mapStateToProps)(HikesScreen);
