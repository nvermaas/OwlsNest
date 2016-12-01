import React from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

// Using ES6 classes instead of React.createClass
// see https://facebook.github.io/react/blog/2015/01/27/react-v0.13.0-beta-1.html
class MyButton extends React.Component {

    constructor(props) {
        console.log('myButton constructor')
        super(props);
        console.log("props=",this.props);

        // initialize state
        this.state = {myClicked: 0,
                      myLabel : this.props.title};

        // bind the eventhandlers to this
        this.handleClick = this.handleClick.bind(this);

        console.log("state = ",this.state);
    }

   // if button is clicked
    handleClick(e) {
       // see https://facebook.github.io/react/docs/events.html
       console.log("handleClick");
       console.log(this);
       this.setState({
            myClicked: this.state.myClicked + 1,
            myLabel : "clicked : "+this.state.myClicked
       })
       console.log('myClicked =',this.state.myClicked);
       console.log('myLabel =',this.state.myLabel);

    }


    render() {
        return (
            <MuiThemeProvider>
                <RaisedButton label={this.state.myLabel} onClick={this.handleClick} />
            </MuiThemeProvider>
        )
    }
}

export default MyButton;