import React from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const MyAwesomeReactComponent = () => (
    <MuiThemeProvider>
        <RaisedButton label="Click Me!" />
    </MuiThemeProvider>
);

export default MyAwesomeReactComponent;