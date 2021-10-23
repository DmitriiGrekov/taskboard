import React, { Component } from "react";

export default class AuthMenu extends Component {


  refresh_vision = (e) => {
    e.preventDefault()
    console.log('hello')
    this.props.refresh_task_vision()
  }

  render() {

    if (this.props.auth) {
      return (
        <div className="auth">
          <ul>
            <li>
              <a href="" id="">
                {this.props.username}
              </a>
            </li>
            <li>
              <a href="" id="logout_user" onClick={this.props.logout_user_func}>
                Выйти
              </a>
            </li>
          </ul>

          <button className="btn btn-primary " id="add_task_button" onClick={this.refresh_vision}>
            +
          </button>
        </div>
      );
    } else {
      return (
        <div className="auth">
          <ul>
            <li>
              <a href="" id="login_button">
                Войти
              </a>
            </li>
            <li>
              <a href="" id="register_button">
                Зарегестрироваться
              </a>
            </li>
          </ul>

          {this.props.auth ? 
          (<button className="btn btn-primary " id="add_task_button" onClick={this.refresh_vision}>
            +
          </button>) : <></>}
          
        </div>
      );
    }
  }
}
