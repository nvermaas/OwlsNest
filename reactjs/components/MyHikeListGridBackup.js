
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
import {GridList, GridTile} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import Subheader from 'material-ui/Subheader';
import StarBorder from 'material-ui/svg-icons/toggle/star-border';
import ActionExplore from 'material-ui/svg-icons/action/explore';
import ActionHome from 'material-ui/svg-icons/action/home';

const styles = {
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  },
  gridList: {
    width: 1500,
    height: 1000,
    overflowY: 'auto',
  },
  image50: {
    width: 200,
    height: 100
  },
  cardStyle: {
    width: 500,
    height: 400
   },
};

const muiTheme = getMuiTheme({
  palette: {
    accent1Color: deepOrange500,
  },
});



var MyHikeListGrid = React.createClass({

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

            var myHikeNodesGrid = this.state.data.results.map(
                function(results){
                    var cardStyle = {
                    width: '300',

                 }
                return <GridTile

                        key={results.hike_image}
                        title={results.title}
                        subtitle={<span> {results.place} </span>}
                        actionIcon={<IconButton><ActionExplore color="white" /></IconButton>}
                       >
                          <img src={results.hike_image} />
                    </GridTile>
            })
        }
        return (
            <MuiThemeProvider>
            <div>
                <GridList cellHeight={180} cols={5} style={styles.gridList}>
                    {myHikeNodesGrid}
                </GridList>
            </div>
            </MuiThemeProvider>
        )
    }
})

export default MyHikeListGrid;
