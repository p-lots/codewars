function NameMe(first, last) {
    this.firstName = first;
    this.lastName = last;
    return {firstName: first, lastName: last, name: this.firstName + ' ' + this.lastName};
}
