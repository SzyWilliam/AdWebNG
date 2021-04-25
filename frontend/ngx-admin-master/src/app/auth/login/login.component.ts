// import
import { ChangeDetectorRef, Component, Inject } from '@angular/core';
import { NB_AUTH_OPTIONS, NbAuthService, NbLoginComponent } from '@nebular/auth';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'ngx-login',
  templateUrl: './login.component.html',
})
export class NgxLoginComponent extends NbLoginComponent {

  constructor(service: NbAuthService, @Inject(NB_AUTH_OPTIONS) options: {},
              cd: ChangeDetectorRef, router: Router, private auth: AuthService) {
    super(service, options, cd, router);
    localStorage.setItem('token', null);
    localStorage.setItem('user', null);
  }

  login() {
    // console.log(this.user);
    this.auth.login(this.user);
  }
}
