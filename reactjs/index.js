var React = require('react')
var ReactDOM = require('react-dom')

var HikeList = React.createClass({
    loadHikesFromServer: function(){
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
        return {data: []};
    },

    componentDidMount: function() {
        this.loadHikesFromServer();
        setInterval(this.loadHikesFromServer,
                    this.props.pollInterval)
    },
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var hikeNodes = this.state.data.map(function(hike){
                return <li> {hike.title} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {hikeNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<HikeList url='/hiking/rest' pollInterval={1000} />,
    document.getElementById('myMainContainer'))