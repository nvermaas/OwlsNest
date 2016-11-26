
// https://toddmotto.com/react-create-class-versus-component/
// https://facebook.github.io/react/docs/state-and-lifecycle.html
// http://www.material-ui.com/#/components/card

import {List, ListItem} from 'material-ui/List';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {grey400,darkBlack, lightBlack, deepOrange500} from 'material-ui/styles/colors';
import Avatar from 'material-ui/Avatar';

import FlatButton from 'material-ui/FlatButton';
import {GridList, GridTile} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import Subheader from 'material-ui/Subheader';
import ActionExplore from 'material-ui/svg-icons/action/explore';
import MapsEditLocation from 'material-ui/svg-icons/maps/edit-location';


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

};


class MyHikeListGrid extends React.Component {

    constructor(props) {
        console.log("constructor")
        super(props);

        this.handleTouchTap = this.handleTouchTap.bind(this);

        this.state = {data: ''};

        // from now on::
        // Wrong   = this.state.data = '';
        // Correct = this.setState({data: ''});
    }

    // if icon is clicked
    handleTouchTap() {
       console.log("handleTouchTap")
       this.setState({data: ''});
    }

   loadHikesFromServer() {
        console.log("loadHikesFromServer")
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    }

    componentDidMount() {
        console.log("componentDidMount")
        this.loadHikesFromServer();
        setInterval(this.loadHikesFromServer, this.props.pollInterval)
    }

    render() {
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
                        title={<span>{results.title} {results.year}</span>}
                        subtitle={<span> {results.place} </span>}
                        actionIcon={
                            //<IconButton onTouchTap={this.handleTouchTap}>
                            <IconButton>
                                <MapsEditLocation color="white" />
                            </IconButton>
                           }
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
}

export default MyHikeListGrid;
