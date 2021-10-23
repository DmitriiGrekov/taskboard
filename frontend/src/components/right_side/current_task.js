import React, { Component } from "react";

export default class CurrentTask extends Component {
    constructor(props){
        super(props)
    }

    
    
  render() {
      
    return (
      <div style={{display: this.props.current_task_vision ? "block": "none"}} class="card">
        <div class="card-header">{this.props.task_title}</div>
        <div class="card-body">
          <blockquote class="blockquote mb-0">
            <p>
                {this.props.task_content}
            </p>
            <footer class="blockquote-footer">
                {this.props.task_date_ending}
            </footer>

            <a href="#" class="btn btn-primary">
                Изменить
            </a>
          </blockquote>
        </div>
      </div>
    );
  }
}
