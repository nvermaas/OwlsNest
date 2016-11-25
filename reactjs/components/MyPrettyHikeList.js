
// https://toddmotto.com/react-create-class-versus-component/
// https://facebook.github.io/react/docs/state-and-lifecycle.html
// http://www.material-ui.com/#/components/card

import {List, ListItem} from 'material-ui/List';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {grey400,darkBlack, lightBlack, deepOrange500} from 'material-ui/styles/colors';
import Avatar from 'material-ui/Avatar';
import Divider from 'material-ui/Divider';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import FlatButton from 'material-ui/FlatButton';

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

const muiTheme = getMuiTheme({
  palette: {
    accent1Color: deepOrange500,
  },
});

var MyPrettyHikeList = React.createClass({

    loadHikesFromServer: function(){
        console.log("loadHikesFromServer")
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        console.log("getInitialState")
        return {data: ''};
    },

    componentDidMount: function() {
        console.log("componentDidMount")
        this.loadHikesFromServer();
        setInterval(this.loadHikesFromServer,
                    this.props.pollInterval)
    },

    render: function() {
        console.log('render')

        if (this.state.data) {
            console.log('DATA!')

            var myPrettyHikeNodes = this.state.data.results.map(
                function(results){
                    var cardStyle = {
                    width: '30%',

                 }
                return <Card style={cardStyle}>
                    <CardHeader
                        title={results.title}
                        subtitle={results.year}
                        actAsExpander={true}
                        showExpandableButton={true}
                     />
                     <CardMedia
                           overlay={<CardTitle title={results.place} subtitle={results.duration} />}
                      >
                        <img class="image50" src={results.hike_image} />
                     </CardMedia>

                      <CardActions>
                        <FlatButton label="Details" />
                        <FlatButton label="Delete" />
                       </CardActions>
                   </Card>
            })
        }
        return (
            <MuiThemeProvider>
            <div>

                <ul>

                        {myPrettyHikeNodes}
                </ul>

            </div>
            </MuiThemeProvider>
        )
    }
})

export default MyPrettyHikeList;
