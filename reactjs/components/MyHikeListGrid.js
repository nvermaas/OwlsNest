
// https://toddmotto.com/react-create-class-versus-component/
// https://facebook.github.io/react/docs/state-and-lifecycle.html
// http://www.material-ui.com/#/components/card

import {List, ListItem} from 'material-ui/List';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {grey400,darkBlack, lightBlack, deepOrange500} from 'material-ui/styles/colors';
import Avatar from 'material-ui/Avatar';

import {GridList, GridTile} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import Subheader from 'material-ui/Subheader';
import ActionExplore from 'material-ui/svg-icons/action/explore';
import MapsEditLocation from 'material-ui/svg-icons/maps/edit-location';
import RaisedButton from 'material-ui/RaisedButton';

// myComponents
//import MyAppBarExample from '/components/MyAppBar';

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
  gridTileStyle: {
    fontFamily: "Raleway",
    fontSize: 32,
  },
};


class MyHikeListGrid extends React.Component {

    constructor(props) {
        console.log("constructor")
        super(props);

        console.log("this.props = ",this.props)

        // bind the functions to 'this'
         // see http://stackoverflow.com/questions/29732015/value-of-this-in-react-event-handler
        this.loadHikesFromServer = this.loadHikesFromServer.bind(this);
        this.handleTouchTap = this.handleTouchTap.bind(this);
        this.handleClick = this.handleClick.bind(this);

        this.state = {data: ''};

        // from now on::
        // Wrong   = this.state.data = '';
        // Correct = this.setState({data: ''});
    }

    // if icon is touchTapped
    handleTouchTap() {
       console.log("handleTouchTap")
       alert('touchTap!!');
       //this.setState({data: ''});
    }

    // if icon is clicked
    handleClick() {
       console.log("handleClick")
       console.log(this)
       alert('click!');
       //this.setState({data: ''});
    }

   loadHikesFromServer() {
        console.log("loadHikesFromServer(",this.props,")")
        //console.log("this.props = ",this.props)
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
                //function(results){
                (results) => {
                return <GridTile style = {styles.gridTileStyle}
                        key={results.hike_image_url}
                        title={<span>{results.title} {results.year}</span>}
                        subtitle={<span> {results.place} </span>}

                        actionIcon={
                            <IconButton onTouchTap={this.handleTouchTap} onClick={this.handleClick}>
                                <MapsEditLocation color="white" />
                            </IconButton>
                           }
                       >
                          <img src={results.hike_image_url} />
                    </GridTile>

            })
        }
        return (
            <MuiThemeProvider>

            <div>
                {this.props.children}
                <GridList cellHeight={200} cols={5} style={styles.gridList}>
                    {myHikeNodesGrid}
                </GridList>
            </div>
            </MuiThemeProvider>
        )
    }
}

export default MyHikeListGrid;
