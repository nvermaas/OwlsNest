import React from 'react';
import FlatButton from 'material-ui/FlatButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {blue500,darkBlack, lightBlack, white} from 'material-ui/styles/colors';

const styles = {

  buttonStyle: {
    fontFamily: "Raleway",
    color: white,
    backgroundColor: 'transparent',
  },
};

// Using ES6 classes instead of React.createClass
// see https://facebook.github.io/react/blog/2015/01/27/react-v0.13.0-beta-1.html
class MyHomeButton extends React.Component {

    constructor(props) {
        console.log('MyHomeButton constructor')
        super(props);
    }

   // if button is clicked
    handleClick(e) {
       // see https://facebook.github.io/react/docs/events.html
       console.log("button.handleClick");

    }


    render() {
        return (
            <MuiThemeProvider>
                <FlatButton labelStyle={styles.buttonStyle} label="Home" onClick={this.handleClick} />
            </MuiThemeProvider>
        )
    }
}

export default MyHomeButton;