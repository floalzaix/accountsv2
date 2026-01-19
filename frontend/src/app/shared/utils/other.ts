/**
   * A small wrapper because when clicked on the button to submit the 
   * blur is gone to quickly and the form is not submitted.
   * 
   * @param callback The close callback of the inplace component.
   * @param event The event that triggered the close.
   */
export function closeInplaceForm(
  callback: (event: any) => void,
  event: any
): void {
setTimeout(() => {
  callback(event);
}, 100);
}