import React, { Component } from "react";
import Switch from "react-switch";
import './App.css';

export default class BasicExample extends Component {
  constructor() {
    super();
    this.state = { controls: {4:{"name":"Tank Light", "status":true}} };
    this.handleChange = this.handleChange.bind(this);
  }

  fetchData() {
    fetch('http://192.168.1.127:5000/api/controls')
    .then(res => res.json())
    .then((data) => {
      this.setState({ controls: data })
    })
    .catch(e => {
      console.log(e);
    });
    setTimeout(this.fetchData.bind(this), 5000);
  }

  componentDidMount() {
    this.fetchData();
  }

  handleChange(checked, event, port) {
    const controls = this.state.controls;

    controls[port]["status"] = checked;

    fetch('http://192.168.1.127:5000/api/controls/'+port, {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        status: checked,
      })
    })
  }

  render() {
    const controls = this.state.controls;
    console.log(controls);

    return (
      <div className="example">
        <h2>Aquarium Control</h2>
        {
          Object.entries(controls)
          .map( ([key, value]) => 
            <div>
              <label>
                <span>{value['name']}</span>
                <Switch
                  id = {key}
                  onChange={this.handleChange}
                  checked={value['status']}
                  className="react-switch"
                />
              </label>
            </div>
          )
        }
      </div>
    );
  }
}

