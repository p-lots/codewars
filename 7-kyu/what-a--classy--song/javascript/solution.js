// code here
class Song {
  constructor(title, artist) {
    this.title = title;
    this.artist = artist;
    this.listeners = [];
  }
  howMany(todaysListeners) {
    let ret = 0;
    for (const listener of todaysListeners) {
      if (!this.listeners.includes(listener.toLowerCase())) {
        ret++;
        this.listeners.push(listener.toLowerCase());
      }
    }
    return ret;
  }
}