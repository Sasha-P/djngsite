import { Injectable }    from '@angular/core';
import { Headers, Http, Response, RequestOptions } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Hero } from './hero';

@Injectable()
export class HeroService {
    

    private heroesUrl = '/api/v1/heroes/';  // URL to web api

    constructor(private http: Http) { }

    getHeroes(): Promise<Hero[]> {
        // let headers = new Headers();
        // headers.append('Access-Control-Allow-Origin', '*');
        // headers.append('Access-Control-Allow-Methods', 'GET, POST, PATCH, PUT, DELETE, OPTIONS');
        // headers.append('Access-Control-Allow-Headers', 'Origin, Content-Type, X-Auth-Token');
        // let options = new RequestOptions({ headers: headers });
        return this.http.get(this.heroesUrl)
                   .toPromise()
                   .then(this.extractData)
                   .catch(this.handleError);
    }

    private extractData(res: Response) {
        //response => response.json().data as Hero[]
        let body = res.json();
        return body.results || { };
    }

    getHero(id: number): Promise<Hero> {
        return this.getHeroes().then(heroes => heroes.find(hero => hero.id === id));
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }
}
