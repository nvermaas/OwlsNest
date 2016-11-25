
// https://toddmotto.com/react-create-class-versus-component/
// https://facebook.github.io/react/docs/state-and-lifecycle.html
import {List, ListItem} from 'material-ui/List';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {grey400,darkBlack, lightBlack, deepOrange500} from 'material-ui/styles/colors';
import Avatar from 'material-ui/Avatar';
import Divider from 'material-ui/Divider';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';

const styles = {
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
                return <list>
                    <ListItem
                        leftAvatar={<Avatar src={results.hike_image}  />}
                        primaryText={
                            <p> {results.title} &nbsp;&nbsp; {results.year} </p>
                        }
                        secondaryText={
                            <p>
                                <span style={{color: darkBlack}}> {results.place}, {results.country}, {results.duration} </span>
                            </p>
                        }
                        secondaryTextLines={2}
                     />
                    <Divider inset={true} />
                </list>
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
