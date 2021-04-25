import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';
import {of as observableOf} from 'rxjs';

@Injectable()
export class AuthService {

  private _authUrl = 'http://localhost:8000/ws/auth/';
  constructor(private http: HttpClient, private router: Router) {}

  fetchUser() {
    const token = localStorage.getItem('token');
    const user = localStorage.getItem('user');
    if (token == null || user == null) {
      localStorage.setItem('token', null);
      localStorage.setItem('user', null);
      this.router.navigateByUrl('/auth/login').then(r => {});
    } else {
      // console.log(JSON.parse(user));
      return observableOf(JSON.parse(user));
    }
  }

  register(user) {
    this.http.post<any>(this._authUrl + 'register', user).subscribe(
      res => {
        // console.log(res);
        localStorage.setItem('token', JSON.stringify(res.token));
        localStorage.setItem('user', JSON.stringify(res.user));
        this.router.navigateByUrl('/pages/search').then(r => {});
      },
      err => {
        // console.log(err);
      },
    );
  }

  login(user) {
    this.http.post<any>(this._authUrl + 'login', user).subscribe(
      res => {
        // console.log(res);
        localStorage.setItem('token', JSON.stringify(res.token));
        localStorage.setItem('user', JSON.stringify(res.user));
        this.router.navigateByUrl('/pages/search').then(r => {});
      },
      err => {
        // console.log(err);
      },
    );
  }
}
