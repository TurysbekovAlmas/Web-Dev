import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [FormsModule, RouterModule], // Добавляем FormsModule и RouterModule
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent {
  album = { id: 1, title: 'My Album' };
}
