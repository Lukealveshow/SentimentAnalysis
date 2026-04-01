import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SentimentService } from './services/sentiment.service';
import { HttpClientModule } from '@angular/common/http';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent {

  text: string = '';
  result: any = null;
  loading: boolean = false;

  constructor(private sentimentService: SentimentService, private cd: ChangeDetectorRef) {}

  analyze() {
  if (!this.text.trim()) return;

  this.loading = true;
  this.result = null;

  this.sentimentService.analyze(this.text).subscribe({
    next: (res) => {
      console.log("RESPOSTA:", res);

      this.result = res;
      this.loading = false;

      this.cd.detectChanges(); 
    },
    error: (err) => {
      console.error(err);
      this.loading = false;

      this.cd.detectChanges(); 
    }
  });
}
  clear() {
  this.text = '';
  this.result = null;
}
}