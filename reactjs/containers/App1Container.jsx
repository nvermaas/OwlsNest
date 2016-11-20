import React from "react"

import Headline from "../components/Headline"

export default class App1Container extends React.Component {
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>App1, complex stuff. Dit moet eerst door webpack voordat het zichtbaar wordt?</Headline>
          </div>
        </div>
      </div>
    )
  }
}