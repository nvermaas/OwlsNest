import React from 'react';
import {Tabs, Tab} from 'material-ui/Tabs';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import MapsEditLocation from 'material-ui/svg-icons/maps/edit-location';

import MyHikeList from './MyHikeList';
import MyHikeDetails from './MyHikeDetails';

import MyOverviewButton from './MyOverviewButton';
import myStore from '../myStore';

const styles = {
  headline: {
    fontSize: 24,
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 400,
    fontFamily: "Raleway",
  },
};

class MyTabs extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      value: 'tabOverview',
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleActive = this.handleActive.bind(this);
    this.handleClickOverview = this.handleClickOverview.bind(this);
    this.handleClickDetails = this.handleClickDetails.bind(this);
  }

  handleActive = (value) => {
    console.log("MyTabs.handleActive");
    this.setState({
      value: value,
    });
    console.log(this.state);
  };

  handleChange = (value) => {
    console.log("MyTabs.handleChange");
    this.setState({
      value: value,
    });
    console.log(this.state);
  };

  handleClickOverview() {
    console.log("MyTabs.handleClickOverview()");
    this.setState({
      value: 'tabOverview',
    });

    // reload the hikinglist
    var myUrl = "http://localhost:8000/hiking/rest"; // replace with redux selector and mapStateToProps
    myStore.dispatch({type: "LOAD_ALL_FROM_SERVER", payload: myUrl});
    console.log(this.state);
  };

  handleClickDetails() {
    console.log("MyTabs.handleClickDetails()");
    this.setState({
      value: 'tabDetails',
    });
    console.log(this.state);

  };


  render() {
    return (
        <MuiThemeProvider>
            <Tabs value={this.state.value} onChange={this.handleChange}>

                <Tab label="Overview" value="tabOverview" onClick={this.handleClickOverview} >
                  <div>
                    <MyHikeList/>
                  </div>
                </Tab>

                <Tab label="Details" value="tabDetails" onClick={this.handleClickDetails}>
                  <div>
                    <MyHikeDetails/>
                  </div>
                </Tab>
             </Tabs>
        </MuiThemeProvider>
    );
  }
}

export default MyTabs;
