import React from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import FlatButton from 'material-ui/FlatButton';

const styles = {
  myImage: {
    width: 500,
    height: 300
  },

  container: {
    textAlign: 'center',
    paddingTop: 200,
  },
};


// Using ES6 classes instead of React.createClass
// see https://facebook.github.io/react/blog/2015/01/27/react-v0.13.0-beta-1.html
class MyHikeDetails extends React.Component {

    constructor(props) {
        console.log('MyHikeDetails constructor')
        super(props);

        // initialize state
        var hike = {title   : "myTitle",
                    year    : 2017,
                    place   : "myPlace",
                    duration: "myDuration",
                    image   : "http://nvermaas.home.xs4all.nl/hiking/media/usa2015.jpg"}

        this.state = {hike: hike};


        // bind the eventhandlers to this
        this.handleClick = this.handleClick.bind(this);

        console.log("state = ",this.state);
    }

   // if button is clicked
    handleClick(e) {
       // see https://facebook.github.io/react/docs/events.html
       console.log("MyHikeDetails.handleClick");

    }


    render() {
        return (
            <MuiThemeProvider>
                <Card>
                    <CardHeader
                        title={this.state.hike.title}
                        subtitle={this.state.hike.year}
                        actAsExpander={true}
                        showExpandableButton={true}
                     />
                     <CardMedia
                           overlay={<CardTitle title={this.state.hike.place} subtitle={this.state.hike.duration} />}
                      >
                        <img className="styles.myImage" src={this.state.hike.image} />
                     </CardMedia>

                      <CardActions>
                        <FlatButton label="Edit" />
                        <FlatButton label="Delete" />
                       </CardActions>
                   </Card>
            </MuiThemeProvider>
        )
    }
}

export default MyHikeDetails;