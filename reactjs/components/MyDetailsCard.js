import React from 'react';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import RaisedButton from 'material-ui/RaisedButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const styles = {

  image50: {
    width: 200,
    height: 100
  },

  container: {
    textAlign: 'center',
    paddingTop: 200,
  },
};

class MyDetailsCard extends React.Component {

    constructor(props) {
        console.log('myCardDetails constructor')
        super(props);
        console.log("props=",this.props);

        // initialize state
        this.state = {myResult: ''}

        // bind the eventhandlers to this
        this.handleClickOK = this.handleClickOK.bind(this);

        console.log("state = ",this.state);
    }

   // if button is clicked
    handleClickOK(e) {
       // see https://facebook.github.io/react/docs/events.html
       console.log("handleClickOK");
    }

    render() {
        return (
            <MuiThemeProvider>
                <Card style={cardStyle}>
                    <CardHeader
                        title={myResult.title}
                        subtitle={myResult.year}
                        actAsExpander={true}
                        showExpandableButton={true}
                     />
                     <CardMedia
                           overlay={<CardTitle title={myResult.place} subtitle={myResult.duration} />}
                      >
                        <img class="Styles.image50" src={myResult.hike_image} />
                     </CardMedia>

                      <CardActions>
                        <FlatButton label="Save" onClick={this.handleClickOK}/>
                        <FlatButton label="Delete" />
                       </CardActions>
                   </Card>
            </MuiThemeProvider>
        )
    }
}

export default MyDetailsCard;