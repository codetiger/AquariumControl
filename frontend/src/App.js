import React, { Component } from "react";
import Switch from '@material-ui/core/Switch';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import SettingsRemoteIcon from '@material-ui/icons/SettingsRemote';

import { ThemeProvider } from '@material-ui/core/styles';
import { createMuiTheme } from '@material-ui/core/styles';
import { deepPurple } from "@material-ui/core/colors";

import './App.css';

const theme = createMuiTheme({
  palette: {
    primary: deepPurple,
  },
});

export default class BasicExample extends Component {
  constructor() {
    super();
    this.state = { controls: {4:{"name":"Tank Light", "status":true}, 6:{"name":"Plant Light", "status":false}} };
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
    console.log(checked);

    if(port in controls)
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
  
    return (
      <ThemeProvider theme={theme}>
        <div className="example">
          <AppBar position="static" color="primary">
            <Toolbar>
              <Typography variant="h6">
                Aquarium Control Panel
              </Typography>
            </Toolbar>
          </AppBar>
          {
            Object.entries(controls)
            .map( ([key, value]) => 
              <div>
                <List>
                  <ListItem>
                    <ListItemAvatar>
                      <Avatar>
                        <SettingsRemoteIcon color="primary"/>
                      </Avatar>
                    </ListItemAvatar>
                    <ListItemText primary={value['name']} secondary={value['name']} />
                    <Switch
                      id = {key}
                      onChange={this.handleChange}
                      checked={value['status']}
                      color="primary"
                    />
                  </ListItem>
                  <Divider>

                  </Divider>
                </List>
              </div>
            )
          }
        </div>
      </ThemeProvider>
    );
  }
}

