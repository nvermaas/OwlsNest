
// https://toddmotto.com/react-create-class-versus-component/
// https://facebook.github.io/react/docs/state-and-lifecycle.html
var React = require('react')
var ReactDOM = require('react-dom')

var HikeList = React.createClass({

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

            var hikeNodes = this.state.data.results.map(
                function(results){
                return <li> {results.title} {results.year} - {results.place}, {results.country}, {results.duration} - {results.hike_image}</li>
            })
        }
        return (
            <div>
                <h1>myBundle.js : HikeList (25 nov 09:53):</h1>
                <ul>
                    {hikeNodes}
                </ul>

            </div>
        )
    }
})

export default HikeList;
