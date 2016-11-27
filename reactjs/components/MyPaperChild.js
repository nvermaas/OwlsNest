import React from 'react';
import Paper from 'material-ui/Paper';
import Avatar from 'material-ui/Avatar';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const style = {
  height: 100,
  width: 100,
  margin: 20,
  textAlign: 'center',
  display: 'inline-block',
};

class MyPaperChild extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
      return (
            <MuiThemeProvider>
              <div>
                <Paper style={style} zDepth={1} />
                <Paper style={style} zDepth={2} />
                <Paper style={style} zDepth={3} />
                <Paper style={style} zDepth={4} />
                <Paper style={style} zDepth={5} />
              </div>
            </MuiThemeProvider>
        )
    }
}

export default MyPaperChild;